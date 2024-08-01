from pollux_application.application_abstract import ApplicationAbstract
from pollux_model.model_example import ModelExample


class ApplicationExample(ApplicationAbstract):
    def __init__(self):
        super().__init__()

        self.ModelExample = ModelExample()

    def init_parameters(self):
        """Function to initialize model parameters"""
        res_param = dict()

        self.ModelExample.update_parameters(res_param)

    def calculate(self):
        """Function to calculate"""

        # Define input dict u
        u = dict()
        u['ModelExample_input_1'] = self.ModelExample.parameters
        u['ModelExample_input_2'] = self.ModelExample.parameter_1

        # Define state dict x
        x = dict()

        self.calculate_value_1(u, x)
        self.plot()

    def calculate_value_1(self, u, x):

        input_1 = u['ModelExample_input_1']
        input_2 = u['ModelExample_input_2']
        result = ModelExample(input_1, input_2)

        self.parameters['result'] = results

    def plot(self):
        """Function to plot"""

    def get_solution(self):
        """Function to assign output values to self"""
        self.outputs = self.parameters

