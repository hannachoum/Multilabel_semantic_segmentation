from mmseg.datasets.builder import PIPELINES


@PIPELINES.register_module()
class PrintShapes:
    def __call__(self, results):
        print("Image shape:", results["img"].shape)
        print("Ground truth shape:", results["gt_semantic_seg"].shape)
        return results
