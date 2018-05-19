import os

name = ["slicing-slices", "making-slices", "nil-slices", "append", "range", "range-condinued", "exercise-slices", "maps", "map-literals", "map-literals-continued", "mutating-maps", "exercise-maps", "function-vavlues", "function-closures", "exercise=fibonacci-closure", "methods", "methods-funcs",  "methods-continued", "methods-with-pointer-receivers", "inferfaces",
        "interfaces-are-satisfied-implicitly", "stringer", "exercise-stringer", "errors", "exercise-errors", "reader", "exercise-reader", "exercise-rot-reader", "web-servers", "exercise-http-handlers", "images", "exercise-images", "goroutines", "channel", "buffered-channel", "range-and-close", "select", "default-selection", "exercise-equivalent-binary-trees", "exercise-web-crawler"]

i = 39
for j in name:
    os.system("mkdir %s-%s" % (i, j))
    os.system("touch %s-%s/%s-%s.go" % (i, j, i, j))
    i += 1
