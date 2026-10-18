package SyntheticConnection {
    part def Subsystem;
    part def System {
        part a : Subsystem;
        part b : Subsystem;
        connection link connect a to b;
    }
}
