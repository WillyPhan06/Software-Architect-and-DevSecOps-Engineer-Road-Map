#Making Async Client side with tweak is receiving 2 messages from server per loop due to announcement as well
import asyncio

async def client_side_connection():
    reader, writer = await asyncio.open_connection("127.0.0.1",8888)

    for i in range(1,4):
        message = input(f"Enter message {i}: ")
        writer.write(message.encode())
        await writer.drain()
        print(f"Client successfully sent message {i}: {message}")
        data = await reader.read(100)
        print(f"Client received message: {data}")
        data_2 = await reader.read(100)
        print(f"Client received message: {data_2}")
    print("Client out of message count, closing now")
    writer.close()
    print("Client soft closed")
    await writer.wait_closed()
    print("Client finally closed")

asyncio.run(client_side_connection())