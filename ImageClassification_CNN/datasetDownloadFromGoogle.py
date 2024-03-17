from simple_image_download import simple_image_download as simp
response = simp.simple_image_download
response().download('sachin', limit=10) # downloads images to new directory## keywords — for instance -> ‘Sachin’ limit — for instance -> 5

#print(response().urls('batmanjoker', 45))

#response().download('batmanjoker', 5,extensions={'.jpg'})
#print(response().urls('batmanjoker', 5,extensions={'.jpg'}))