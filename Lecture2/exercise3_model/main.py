
import torch
from torch.nn import Module


class ExerciseModel(Module):
    
    """ コンストラクタ """
    def __init__(self, mytensor: torch.Tensor, elem_add: int, elem_multiply: int):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    """ Forward """
    def forward(self, x: torch.Tensor):
        # 入力とテンソルの形状が同じか確認
        assert x.size() == self.mytensor.size(), "input size must match self.tensor size."

        problem2_out = x + self.mytensor # テンソルを加算
        problem3_out = problem2_out + self.elem_add # 数値を加算
        problem4_out = problem3_out * self.elem_multiply # 数値を乗算

        return problem2_out, problem3_out, problem4_out


if __name__=="__main__":
    mymodel = ExerciseModel(torch.ones((3, 3)), 4, 6)
    
    p2out, p3out, p4out = mymodel(torch.full((3, 3), 2))
    
    """ 各テンソルを出力 """
    print("===== problem 2 =====")
    print(repr(p2out))
    print("===== problem 3 =====")
    print(repr(p3out))
    print("===== problem 4 =====")
    print(repr(p4out))
