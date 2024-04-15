class ZerosFuncoes:
    name = "Zeros de funções base"

    def get_new_point(self):
        raise Exception("Método ainda não implementado")

    def get_f_new_point(self):
        return self.f(self.get_new_point())

    def step(self):
        raise Exception("Método ainda não implementado")

    def calculate_root(self):
        raise Exception("Método ainda não implementado")
