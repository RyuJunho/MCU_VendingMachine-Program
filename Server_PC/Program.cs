using System;
using System.Text;
using System.Net;
using System.Net.Sockets;
using System.IO.Ports;
using System.Threading;

namespace MCU_002_6_Server
{
    class Program
    {
        public static int PORT = 9090;
        static void Main(string[] args)
        {

            SerialPort sp = new SerialPort("Com11");
            sp.BaudRate = 9600;
            sp.DataBits = 8;
            sp.Parity = Parity.None;
            sp.StopBits = StopBits.One;
            sp.Open();


            using (var server = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
            {
                server.Bind(new IPEndPoint(IPAddress.Any, 9090));
                server.Listen(20);

                Console.WriteLine("서버 시작");
                Console.WriteLine();
                try
                {
                    while (true)
                    {
                        ThreadPool.QueueUserWorkItem(c =>
                        {
                            Socket client = (Socket)c;
                            try
                            {
                                while (true)
                                {
                                    string command = sp.ReadLine();

                                    command = command.Replace("\r", string.Empty);


                                    if (command == "1" || command == "2")
                                    {
                                        var msg = "";
                                        if (command == "1") { msg = "제품1"; }
                                        else if (command == "2") { msg = "제품2"; }
                                        Console.Write(msg);
                                        Console.WriteLine(" 구매");

                                        //메시지(msg)를 클라이언트로 전송
                                        var data = Encoding.UTF8.GetBytes(msg);
                                        client.Send(BitConverter.GetBytes(data.Length));
                                        client.Send(data, data.Length, SocketFlags.None);
                                    }
                                }
                            }
                            catch (Exception)
                            {
                                client.Close();
                            }
                        }, server.Accept());
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
            Console.WriteLine("Press any key.");
            Console.ReadLine();
        }
    }
}