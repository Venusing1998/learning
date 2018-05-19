import os

name = ["hello", "sandbox", "packages", "imports", "exported-names", "functions", "functions-continued", "multiple-results", "named-results", "variables", "variables-with-initializers", "short-variable-declarations", "basic-types", "zero", "type-conversions", "type-interence", "constants", "numeric-constants", "for", "for-continued", "for-is-gos-while", "forever", "if", "if-with-a-short-statement", "if-and-else", "exercise-loops-and-functions", "switch", "switch-evaluation-order", "switch-with-no-condition", "defer", "defer-multi", "pointers", "structs", "struct-fields", "struct-pointers", "struct-literals", "array", "slices", "slices-pointers", "slice-literals", "slice-bounds", "slice-len-cap", "nil-slices", "making-slices", "slices-of-slice", "append", "range", "range-condinued", "exercise-slices", "maps", "map-literals",
        "map-literals-continued", "mutating-maps", "exercise-maps", "function-vavlues", "function-closures", "exercise-fibonacci-closure", "methods", "methods-funcs",  "methods-continued", "methods-pointers", "methods-pointers-explained", "indirection", "indirection-values", "methods-with-pointer-receivers", "inferfaces", "interfaces-are-satisfied-implicitly", "interface-values", "interface-values-with-nil", "nil-interface-values", "empty-interface", "type-assertions", "type-switches", "stringer", "exercise-stringer", "errors", "exercise-errors", "reader", "exercise-reader", "exercise-rot-reader", "images", "exercise-images",  "goroutines", "channels", "buffered-channels", "range-and-close", "select", "default-selection", "exercise-equivalent-binary-trees", "mutex-counter", "exercise-web-crawler"]

i = 1
for j in name:
    os.system("mkdir %s-%s" % (i, j))
    os.system("touch %s-%s/%s-%s.go" % (i, j, i, j))
    i += 1
