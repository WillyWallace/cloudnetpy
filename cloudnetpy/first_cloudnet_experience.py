from cloudnetpy.mira import mira2nc
from cloudnetpy.categorize import generate_categorize
from cloudnetpy.products.classification import generate_class

path = '/home_local/afoth/programming/Cloudnet_Test_Data/'

mira2nc(path + '20181204_mace-head_mira_raw.nc', path + '20181204_mace-head_mira.nc', {'name': 'Mace-Head'})


input_files = {
    'radar': path + '20181204_mace-head_mira.nc',
    'lidar': path + '20181204_mace-head_chm15k.nc',
    'model': path + '20181204_mace-head_ecmwf.nc',
    'mwr': path + '20181204_mace-head_hatpro.nc'
    }
generate_categorize(input_files, path + 'categorize.nc')

generate_class(path + 'categorize.nc', path + 'classification.nc')
