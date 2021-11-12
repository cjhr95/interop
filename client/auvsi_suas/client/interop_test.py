import client
import interop_api_pb2


#client = client.Client(url='http://192.168.74.128:8000', username='testuser', password='testpass')
client = client.Client(url='http://192.168.74.128:8000', username='testuser', password='testpass')

odlc = interop_api_pb2.Odlc()
odlc.type = interop_api_pb2.Odlc.STANDARD
odlc.latitude = 38
odlc.longitude = -76
odlc.orientation = interop_api_pb2.Odlc.N
odlc.shape = interop_api_pb2.Odlc.SQUARE
odlc.shape_color = interop_api_pb2.Odlc.GREEN
odlc.alphanumeric = 'A'
odlc.alphanumeric_color = interop_api_pb2.Odlc.WHITE
odlc.mission = 1

odlc = client.post_odlc(odlc)

with open('./testdata/A.jpg', 'rb') as f:
    image_data = f.read()
    client.put_odlc_image(odlc.id, image_data)