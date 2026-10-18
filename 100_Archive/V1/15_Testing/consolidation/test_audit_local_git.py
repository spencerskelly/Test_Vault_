#!/usr/bin/env python3
"""Offline disposable-fixture verification for the Mac/Linux Step 06 inventory script."""
import os, pathlib, shutil, subprocess, tempfile, unittest

AUDIT = pathlib.Path(__file__).with_name('audit_local_git.sh').resolve()
ROOT = None

def git(cwd,*args,check=True):
    r=subprocess.run(['git',*args],cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env={**os.environ,'GIT_AUTHOR_NAME':'Fixture','GIT_AUTHOR_EMAIL':'fixture@example.invalid','GIT_COMMITTER_NAME':'Fixture','GIT_COMMITTER_EMAIL':'fixture@example.invalid'},check=False)
    if check and r.returncode:
        raise RuntimeError(f'git {args}: {r.stderr}')
    return r.stdout.strip()

def run(path):
    return subprocess.run(['sh',str(AUDIT),str(path)],capture_output=True,text=True,timeout=15)

def make_local(path):
    path.mkdir()
    git(path,'init','-q','-b','main')
    git(path,'config','user.name','Fixture')
    git(path,'config','user.email','fixture@example.invalid')
    (path/'file.txt').write_text('one\n')
    git(path,'add','file.txt')
    git(path,'commit','-qm','initial')
    return path

def make_tracking(tmp):
    bare=tmp/'bare.git';bare.mkdir()
    git(bare,'init','-q','--bare','-b','main')
    seed=make_local(tmp/'seed')
    git(seed,'remote','add','origin',str(bare))
    git(seed,'push','-q','-u','origin','main')
    clone=tmp/'clone'
    git(tmp,'clone','-q',str(bare),str(clone))
    git(clone,'config','user.name','Fixture');git(clone,'config','user.email','fixture@example.invalid')
    return clone,seed,bare

class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='mdse-step06-')
        self.tmp=pathlib.Path(self.temp.name)
    def tearDown(self): self.temp.cleanup()
    def audit(self,path):
        r=run(path)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIn('ARCHIVE_SIGNOFF=NOT_CERTIFIED',r.stdout)
        self.assertIn('FETCH_PERFORMED=false',r.stdout)
        self.assertNotIn('file.txt',r.stdout)
        return r.stdout
    def test_clean_remote_tracking(self):
        clone,_,_=make_tracking(self.tmp)
        out=self.audit(clone)
        self.assertIn('STATUS=REMOTE_TRACKING_ONLY_NOT_VERIFIED',out)
        self.assertIn('REMOTE_COUNT=1',out)
        self.assertIn('TRACKED_DIRTY_ENTRIES=0',out)
        self.assertIn('UNTRACKED_ENTRIES=0',out)
    def test_local_ahead_untracked_tracked_and_index_unchanged(self):
        clone,_,_=make_tracking(self.tmp)
        (clone/'file.txt').write_text('two\n')
        (clone/'local secret.txt').write_text('work\n')
        idx=(clone/'.git/index')
        before=(idx.read_bytes(),idx.stat().st_mtime_ns)
        git(clone,'add','file.txt')
        git(clone,'commit','-qm','ahead')
        (clone/'file.txt').write_text('three\n')
        before=(idx.read_bytes(),idx.stat().st_mtime_ns)
        out=self.audit(clone)
        self.assertIn('STATUS=REVIEW_AHEAD',out)
        self.assertIn('AHEAD=1 BEHIND=0',out)
        self.assertIn('TRACKED_DIRTY_ENTRIES=1',out)
        self.assertIn('UNTRACKED_ENTRIES=1',out)
        self.assertEqual(before,(idx.read_bytes(),idx.stat().st_mtime_ns))
        self.assertNotIn('local secret.txt',out)
    def test_behind_remote_tracking(self):
        clone,seed,_=make_tracking(self.tmp)
        (seed/'file.txt').write_text('two\n');git(seed,'commit','-qam','ahead remote');git(seed,'push','-q')
        git(clone,'fetch','-q','origin') # fixture preparation only; auditor remains offline
        out=self.audit(clone)
        self.assertIn('AHEAD=0 BEHIND=1 STATUS=REVIEW_BEHIND',out)
    def test_diverged_remote_tracking(self):
        clone,seed,_=make_tracking(self.tmp)
        (clone/'file.txt').write_text('local\n');git(clone,'commit','-qam','local ahead')
        (seed/'file.txt').write_text('remote\n');git(seed,'commit','-qam','remote ahead');git(seed,'push','-q')
        git(clone,'fetch','-q','origin')
        out=self.audit(clone)
        self.assertIn('AHEAD=1 BEHIND=1 STATUS=REVIEW_DIVERGED',out)
    def test_untracked_branch_missing_upstream(self):
        loc=make_local(self.tmp/'loc')
        git(loc,'branch','future')
        out=self.audit(loc)
        self.assertIn('LOCAL_BRANCH_COUNT=2',out)
        self.assertIn('BRANCH=future UPSTREAM=NONE',out)
        self.assertIn('STATUS=REVIEW_NO_UPSTREAM',out)
        self.assertIn('REMOTE_COUNT=0',out)
    def test_local_upstream_not_remote_tracking(self):
        loc=make_local(self.tmp/'loc')
        git(loc,'checkout','-qb','topic')
        git(loc,'branch','--set-upstream-to=main','topic')
        out=self.audit(loc)
        self.assertIn('STATUS=REVIEW_LOCAL_UPSTREAM',out)
    def test_detached_head(self):
        loc=make_local(self.tmp/'loc')
        git(loc,'checkout','--detach','-q')
        (loc/'file.txt').write_text('orphan\n');git(loc,'commit','-qam','detached')
        out=self.audit(loc)
        self.assertIn('CURRENT_BRANCH=DETACHED',out)
        self.assertIn('DETACHED_HEAD_REVIEW=REQUIRED',out)
    def test_stash_and_second_worktree(self):
        loc=make_local(self.tmp/'loc')
        (loc/'file.txt').write_text('stash\n')
        git(loc,'stash','-q')
        wt=self.tmp/'other';git(loc,'worktree','add','-q','-b','second',str(wt))
        out=self.audit(loc)
        self.assertIn('STASH_COUNT=1',out)
        self.assertIn('WORKTREE_COUNT=2',out)
    def test_missing_upstream_tracking_ref(self):
        clone,_,_=make_tracking(self.tmp)
        git(clone,'update-ref','-d','refs/remotes/origin/main')
        out=self.audit(clone)
        self.assertIn('STATUS=REVIEW_UPSTREAM_UNRESOLVED',out)
    def test_special_filenames_no_leak(self):
        loc=make_local(self.tmp/'loc')
        (loc/'secret\nline.txt').write_text('private')
        (loc/'file.txt').write_text('dirty')
        out=self.audit(loc)
        self.assertIn('UNTRACKED_ENTRIES=1',out)
        self.assertIn('TRACKED_DIRTY_ENTRIES=1',out)
        self.assertNotIn('secret',out)
    def test_invalid_path_is_failure(self):
        r=run(self.tmp/'does_not_exist')
        self.assertEqual(r.returncode,2)
        self.assertIn('ERROR:',r.stderr)
    def test_unborn_repo_failure(self):
        loc=self.tmp/'empty';loc.mkdir();git(loc,'init','-q','-b','main')
        r=run(loc)
        self.assertEqual(r.returncode,2)
        self.assertIn('unborn/invalid HEAD',r.stderr)
    def test_shallow_clone(self):
        _,_,bare=make_tracking(self.tmp)
        loc=self.tmp/'shallow'
        git(self.tmp,'clone','-q','--depth','1',bare.resolve().as_uri(),str(loc))
        out=self.audit(loc)
        self.assertIn('SHALLOW=true',out)
    def test_pipe_character_in_branch_name(self):
        loc=make_local(self.tmp/'loc')
        git(loc,'branch','special|branch')
        out=self.audit(loc)
        self.assertIn('BRANCH=special|branch UPSTREAM=NONE',out)
    def test_unstaged_and_staged_both_single_dirty_entry(self):
        loc=make_local(self.tmp/'loc')
        (loc/'file.txt').write_text('two');git(loc,'add','file.txt')
        (loc/'file.txt').write_text('three')
        out=self.audit(loc)
        self.assertIn('TRACKED_DIRTY_ENTRIES=1',out)

if __name__=='__main__': unittest.main(verbosity=2)
