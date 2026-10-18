package SyntheticNestedParts {
    part def Controller;
    part def Assembly {
        part controller : Controller[1];
        part housing {
            part fastener;
        }
    }
}
