import numpy as np
from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.robots import register_robot_class

from robosuite_models.utils import robosuite_model_path_completion


@register_robot_class("FixedBaseRobot")
class Indy7(ManipulatorModel):
    """
    Indy7 is a single-arm robot, from Neuromeka

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    arms = ["right"]

    def __init__(self, idn=0):
        super().__init__(robosuite_model_path_completion("robots/indy7/robot.xml"), idn=idn)

        # Set joint damping
        self.set_joint_attribute(attrib="damping", values=np.array((0.1, 0.1, 0.1, 0.1, 0.1, 0.01)))

    @property
    def default_base(self):
        return "RethinkMount"

    @property
    def default_gripper(self):
        return {"right": "IndyGripper"}

    @property
    def default_controller_config(self):
        return {"right": "default_indy7"}

    @property
    def init_qpos(self):
        return np.array([0.0, 0.0, -np.pi/2, 0, -np.pi/2, np.pi/2])

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.35 - table_length / 2, 0.0, 0.0),
        }

    @property
    def top_offset(self):
        return np.array((0, 0, 1.0))

    @property
    def _horizontal_radius(self):
        return 0.5

    @property
    def arm_type(self):
        return "single"
