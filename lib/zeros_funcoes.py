class ZerosFuncoes:
    name = "Zeros de funções base"
    finished_by_image = False
    finished_by_domain = False
    domain_error = ["-"]
    image_error = ["-"]
    epsilon = 0.1

    def get_domain_error(self):
        raise Exception("Método ainda não implementado")

    def get_image_error(self):
        return abs(self.get_f_new_point())

    def get_new_point(self):
        raise Exception("Método ainda não implementado")

    def get_f_new_point(self):
        return self.f(self.get_new_point())

    def step(self):
        raise Exception("Método ainda não implementado")

    def calculate_root(self):
        raise Exception("Método ainda não implementado")
