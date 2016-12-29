CAFFE_ROOT=G:/GitHub/caffe/
caffe train -solver ./mvcnn_caffenet_simple/solver.prototxt -weights $CAFFE_ROOT/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0
