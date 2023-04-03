import sys
from time import sleep

import xpc


def monitor():
    with xpc.XPlaneConnect() as client:
        client.sendTEXT("Starting STIL Simulation", -1, -1)
        #client.getDREF('sim/cockpit2/gauges/indicators/heading_AHARS_deg_mag_pilot')
        desired_heading = [0]
        while True:
            # pitch 0, roll 1, rudder 2, trottle 3, gear 4, flaps 5, speedbrake 6

            posi = client.getPOSI();
            ctrl = client.getCTRL();
            current_control_matrix = [ctrl[0],ctrl[1],0,ctrl[3],ctrl[4],ctrl[5],ctrl[6]]
            roll_deg = client.getDREF('sim/cockpit2/gauges/indicators/roll_electric_deg_pilot')
            speed = client.getDREF('sim/flightmodel/position/indicated_airspeed')
            pitch = client.getDREF('sim/cockpit2/gauges/indicators/pitch_electric_deg_pilot')
            heading = client.getDREF('sim/cockpit2/gauges/indicators/heading_AHARS_deg_mag_pilot')

            client.sendDREF('sim/flightmodel/controls/parkbrake', 0)


            if roll_deg[0] < -5:
                current_control_matrix[1] += 0.004

            if roll_deg[0] == 0:
                current_control_matrix[1] = -998

            if roll_deg[0] > 5:
                current_control_matrix[1] -= 0.004

            if pitch[0] < -5:
                current_control_matrix[0] += 0.5

            if pitch[0] == 0:
                current_control_matrix[0] = -998

            if pitch[0] > 5:
                current_control_matrix[0] -= 0.5



            client.sendCTRL(current_control_matrix)
            client.sendTEXT("Loc: (%4f, %4f, %4f)\nAileron:%2f Elevator:%2f Rudder:%2f \nHeading:%2f Airspeed:%2f "
                            "Roll:%2f Pitch:%2f\nControl Matrix\nPitch Input:%2f\nRoll Input:%2f\nRudder Input:%2f" \
                            % (posi[0], posi[1], posi[2], ctrl[1], ctrl[0], ctrl[2], heading[0], speed[0], roll_deg[0],
                               pitch[0], current_control_matrix[0], current_control_matrix[1],
                               current_control_matrix[2]), -1, -1)
            # pitch 0, roll 1, rudder 2, trottle 3, gear 4, flaps 5, speedbrake 6

            print(
                "Loc: (%4f, %4f, %4f) Aileron:%2f Elevator:%2f Rudder:%2f Throttle:%2f Airspeed:%2f Roll:%2f Pitch:%2f\n" \
                % (posi[0], posi[1], posi[2], ctrl[1], ctrl[0], ctrl[2], ctrl[3], speed[0], roll_deg[0], pitch[0]))
            print(desired_heading)
            print(heading)

if __name__ == "__main__":
    monitor()