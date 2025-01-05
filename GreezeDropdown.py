class GreezeDropdown:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "selection": (["High Quality (slow)", "Draft (fast)"], {"default":"Draft (fast)"}),
                "zero-indexed": ("BOOLEAN", {"default":False}),
            },
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "Greeze"

    def test(self):
        return ()
