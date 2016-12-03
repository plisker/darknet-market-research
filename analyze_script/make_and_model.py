import sys
import exifread

def get_make_and_model(file):
    f = open(file, 'rb')
    tags = exifread.process_file(f)
    make = tags["Image Make"]
    model = tags["Image Model"]
    return (make, model)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error! No image file specified!")
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)

    file = sys.argv[1]
    make, model = get_make_and_model(file)
    print "File:", sys.argv[1]
    print "Make:", make
    print "Model:", model