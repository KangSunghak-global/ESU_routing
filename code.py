
def variable_declare(MessageName):
    text = "ubS_F_%s_Ind = STD_OFF;\n"% MessageName
    f = open("EthernetSwc.c", 'a')

    f.write(text)
    f.close()

def Indicate_Function(MessageName):
    text = """FUNC (void, EthernetSwc_CODE)ESU_ETH_%s_Ind(void)
{
    ubS_F_%s_Ind = STD_ON;
}\n\n"""% (MessageName, MessageName)
    f = open("EthernetSwc.c", 'a')

    f.write(text)
    f.close()

def Routing_Function(MessageName, SignalDefine, routingSet):
    text = """static void s_RC_%s(void)
{
%s
    if(ubS_F_%s_Ind == STD_ON)
    {
        %s
        ubS_F_%s_Ind = STD_OFF;
    }
}\n\n"""% (MessageName, SignalDefine, MessageName, routingSet, MessageName)
    f = open("EthernetSwc.c", 'a')

    f.write(text)
    f.close()


def Define_variable(size, signalName):
    if size <= 8:
        type = "uint8"
    elif size<=16:
        type = "uint16"
    else:
        type = "uint32"

    variable_set = "\t%s %s;\n"% (type, signalName)
    
    return variable_set


def Routing(Signal, SrcPort, Message):

    routing_set = """ //it need to check destination port number of Read_Port because it sometimes define with 51954  
    \t%s = Rte_DRead_EthernetSwc_ESU_ETH_%s_%s_51915_%s();
    \tRte_Write_EthernetSwc_ESU_ETH_%s_%s_51914_%s(%s);\n\n"""%(Signal, Message, SrcPort, Signal, Message, SrcPort, Signal, Signal)

    return routing_set