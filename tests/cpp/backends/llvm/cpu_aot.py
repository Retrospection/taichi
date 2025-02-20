import os

import taichi as ti


def compile_aot():
    ti.init(arch=ti.x64)

    @ti.kernel
    def run(base: int, arr: ti.types.ndarray()):
        for i in arr:
            arr[i] = base + i

    arr = ti.ndarray(int, shape=16)
    run(42, arr)

    assert "TAICHI_AOT_FOLDER_PATH" in os.environ.keys()
    dir_name = str(os.environ["TAICHI_AOT_FOLDER_PATH"])

    m = ti.aot.Module(ti.x64)
    m.add_kernel(run, template_args={'arr': arr})
    m.save(dir_name, 'x64-aot')


compile_aot()
