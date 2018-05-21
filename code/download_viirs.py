print "Setting the working directory"
import os
work_dir = os.path.dirname(os.path.realpath(__file__)) # This method returns the directry path of this script.
os.chdir(work_dir)
print work_dir

if not os.path.isdir("../orig/"): # Create the output directory if it doesn't exist
    os.makedirs("../orig/")

if not os.path.isdir("../data/"): # Create the output directory if it doesn't exist
    os.makedirs("../data/")

if not os.path.isdir("../docs/"): # Create the output directory if it doesn't exist
    os.makedirs("../docs/")

### Define the main function ###
def main():
    try:
        print "Download the tar file"
        url = "https://data.ngdc.noaa.gov/instruments/remote-sensing/passive/spectrometers-radiometers/imaging/viirs/dnb_composites/v10//2015/SVDNB_npp_20150101-20151231_75N060W_v10_c201701311200.tgz"
        downloaded_tar = "../orig/SVDNB_npp_20150101-20151231_75N060W_v10_c201701311200.tgz"
        download_data(url, downloaded_tar)

        print "Extract all files" # Extracting only necessary files (the .extract() function) does not work. So we extract all and then delete those unnecessary.
        tempdir = "../temp/"
        uncompress_tar(downloaded_tar, tempdir)

        print "Save files that we need in the appropriate folders"
        # The main light data
        light_tif = "SVDNB_npp_20150101-20151231_75N060W_vcm-orm-ntl_v10_c201701311200.avg_rade9.tif"
        os.rename(tempdir+light_tif, "../data/"+light_tif)
        # Number of cloud-free observations
        cloudfree_tif = "SVDNB_npp_20150101-20151231_75N060W_vcm_v10_c201701311200.cf_cvg.tif"
        os.rename(tempdir+cloudfree_tif, "../data/"+cloudfree_tif)
        # Readme
        readme_txt = "README_dnb_composites_v1.txt"
        os.rename(tempdir+readme_txt, "../docs/"+readme_txt)

        print "Delete the other files that we do not need"
        for file in os.listdir(tempdir):
            print file
            os.remove(tempdir+file)
        print "Deleting temp dir"
        os.rmdir(tempdir)

        print "All done."

    # Return any other type of error
    except:
        print "There is an error."

### Define the subfunctions ###
def download_data(url, output):
    print "...downloading and saving the file"
    import urllib
    urllib.urlretrieve(url, output)

def uncompress_tar(in_tar, outdir):
    print "...creating the output directory if it doesn't exist"
    if not os.path.isdir(outdir): # Create the output directory if it doesn't exist
        os.makedirs(outdir)
    print "...importing the tarfile module"
    import tarfile
    print "...creating a TarFile object"
    tar = tarfile.open(in_tar, "r:gz") ## create a TarFile Object, which allows us to use special functions for interacting with the tar file. The mode is "r:gz", which reads a gzip compression
    print "...extracting all files"
    tar.extractall(path = outdir)

### Execute the main function ###
if __name__ == "__main__":
    main()
