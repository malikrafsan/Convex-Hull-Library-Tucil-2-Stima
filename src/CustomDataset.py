class CustomDataset:
    def __init__(self, dict):
        self.data = dict['data']
        self.target = dict['target']
        self.target_names = dict['target_names']
        self.feature_names = dict['feature_names']
