from client import MultiModalDatasetSyntheticAugmentationEngineClient

def main():
    client = MultiModalDatasetSyntheticAugmentationEngineClient()
    res = client.augment_dataset("/datasets/vision_seed/", 5)
    print(f"Synthetic Samples Generated: {res['synthetic_samples_generated']}")
    print(f"Quality Score: {res['quality_score']}")

if __name__ == "__main__":
    main()
