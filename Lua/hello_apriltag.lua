local uartNum = 4 --Номер UART
local baudRate = 9600 --скорость передачи данных
local stopBits = 1 
local parity = Uart.PARITY_NONE 
local uart = Uart.new(uartNum, baudRate, parity, stopBits) -- создание объекта UART

local leds=Ledbar.new(4) -- объект LedBar, порт управления светодиодами на плате

local function color(r,g,b) -- функция заливки всех светодиодов одним цветом
    for i=0,3,1 do
        leds:set(i,r,g,b)
    end
end

local sync = 0.1 -- задержка синхронизации

local function takeFunc() -- функция обработки сообщений с uart
    inp = uart:read(1)
    if(inp == 'n') then -- лампочки не горят при отсутствии apriltag
        color(0,0,0)
    elseif(inp == '0') then -- красный если id=0
        color(1,0,0)
    elseif(inp == '1') then -- синий если id=1
        color(0,1,0)
    end
end

function callback(event) --Обязательная функция
end

t = Timer.new(sync, takeFunc) --таймер, запускает функцию takeFunc каждые sync секунд
color(0,0,0) 
t:start()

