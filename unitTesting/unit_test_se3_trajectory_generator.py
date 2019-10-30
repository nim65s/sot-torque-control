from dynamic_graph.sot.torque_control.se3_trajectory_generator import SE3TrajectoryGenerator
from dynamic_graph.sot.torque_control.tests.robot_data_test import initRobotData

# Instanciate a pose trajectory generator
initial_value = (1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0.)
se3tg = SE3TrajectoryGenerator("se3tg_test")
se3tg.init(initRobotData.controlDT)
se3tg.initial_value.value = initial_value
se3tg.x.recompute(10)
