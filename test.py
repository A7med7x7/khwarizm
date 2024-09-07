from khwarizm.src.ensembles import Ensembles
models = ['lgbm', 'catboost']
output = Ensembles.ensembles(models=models)
output
