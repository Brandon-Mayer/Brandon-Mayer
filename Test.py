import fiftyone as fo
import fiftyone.zoo as foz

fo.config.desktop_app = True
dataset = foz.load_zoo_dataset("open-images-v6",
                               split="validation",
                               label_types=["detections"],
                               classes=["Handgun", "Rifle"],
                               max_samples=100,
                               dataset_name="open-images-weapons")
session = fo.launch_app(dataset)

session.wait()
