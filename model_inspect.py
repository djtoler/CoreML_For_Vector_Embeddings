import coremltools as ct

# Load MLModel object
model = ct.models.MLModel("SentenceEmbeddingModel.mlpackage")

# Get the spec object
spec = model.get_spec()
print("Model type: {}".format(spec.WhichOneof('Type')))