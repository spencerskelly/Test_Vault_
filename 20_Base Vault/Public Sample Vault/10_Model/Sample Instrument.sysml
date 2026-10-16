// SYNTHETIC demonstration only. Independent parser validation pending.
package FictionalLibrary {
    port def SignalPort;
    part def ControlUnit {
        port input : SignalPort;
    }
    part def SensorUnit {
        port output : SignalPort;
    }
    part def PowerUnit;
    part def OperatorPanel;
}
package FictionalProduct {
    part def SampleInstrument {
        part control : FictionalLibrary::ControlUnit;
        part sensor : FictionalLibrary::SensorUnit;
        part power : FictionalLibrary::PowerUnit;
        part panel : FictionalLibrary::OperatorPanel;
        connect sensor.output to control.input;
    }
}
