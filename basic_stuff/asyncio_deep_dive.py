'''
Aprofundamento no uso de operações assíncronas com Python, focado especialmente
nas formas mais modernas de assíncronia, como async/await e asyncio,
lidando com operações concorrentes

O módulo asyncio lida com concorrência utilizando coroutines, disparando processos
leves ao invés de utilizar novas threads de sistema, atuando análogas as
goroutines em Go
'''
import asyncio
from asyncio import subprocess


# Declara uma nova coroutine utilizando a keyword "async". Coroutines atuam
# em seu núcleo como se fossem geradores assíncronos
async def hello_world(identifier):
    print(f'Hello {identifier}')

    # Await é a keyword responsável por passar o controle da função de volta
    # ao loop de eventos, suspendendo a execução da função exterior até que
    # o resultado de uma coroutine (nesse caso asyncio.sleep(1)) seja
    # processado e retornado
    await asyncio.sleep(1)

    print(f'World {identifier}')


async def exec_gather():
    # asyncio.gather() executa as coroutines passadas em ordem e de forma
    # concorrente, retornando uma lista de resultados ordenados caso todas as
    # coroutines passadas sejam executadas com sucesso
    await asyncio.gather(hello_world(1), hello_world(2), hello_world(3))

    print("")

    # Também é possível utilizar asyncio.gather() a partir de uma list ou tuple
    # comprehension, ou um gerador, passando os argumentos da iteração para
    # a função desejada e desempacotando as operações
    await asyncio.gather(*(hello_world(n) for n in range(4, 10)))


# asyncio.crete_subprocess_shell é usado para criar subprocessos para criar
# e executar comandos que executam assíncronos
async def exec_command(command):
    # Cria um novo subprocesso redirecionando a stdout e a stderr
    process = await asyncio.create_subprocess_shell(command,
                                                    stdout=asyncio.subprocess.PIPE,
                                                    stderr=asyncio.subprocess.PIPE)

    # Executa o comando esperando peloresultado
    stdout, stderr = await process.communicate()

    # Exibe o resultado das operações caso elas não sejam None
    if stdout:
        print(f'Stdout: {stdout.decode()}')

    if stderr:
        print(f'Stderr: {stderr.decode()}')


if __name__ == '__main__':
    # asyncio.run executa a coroutine passada, gerenciando o loop de eventos
    # e retornando seu resultado
    asyncio.run(exec_gather())

    print('')

    asyncio.run(exec_command('echo Foo'))

