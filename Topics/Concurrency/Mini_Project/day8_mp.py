#Making Async Echo Server but with own tweak is sending back backward messages with announcement
import asyncio

async def da_server(reader,writer):
    info = writer.get_extra_info("peername")
    print(f"Server received connection from {info}")
    while True:
        data = await reader.read(100)
        if not data:
            print(f"Server not receiving further data from {info}, closing now!")
            break
        print(f"Server received message: {data.decode()}")
        server_pre_message_announce = "Server echoing back backward message"
        writer.write(server_pre_message_announce.encode())
        await writer.drain()
        print("Server sent backward announcement")
        writer.write((data.decode()[::-1]).encode())
        await writer.drain()
        print(f"Server sent backward message: {data.decode()[::-1]}")
    writer.close()
    print("Server soft closed")
    await writer.wait_closed()
    print("Server finally closed")

async def main():
    server = await asyncio.start_server(da_server, '127.0.0.1', 8888)
    server_address = server.sockets[0].getsockname()
    print(f"Server currently serving on {server_address}")

    async with server:
        await server.serve_forever()

asyncio.run(main())