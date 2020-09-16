def MsgNameSet(MsgName):
    text = '\t"%s",\n'% MsgName
    return text

def SrcMACSet(SrcMAC, MsgName):
    text = "\t{%s}, //%s\n"% (SrcMAC, MsgName)
    return text

def DstMACSet(DstMAC, MsgName):
    text = "\t{%s}, //%s\n"% (DstMAC, MsgName)
    return text

def SrcIPSet(SrcIP, MsgName):
    text = "\t{%s}, //%s\n"% (SrcIP, MsgName)
    return text

def DstIPSet(DstIP, MsgName):
    text = "\t{%s}, //%s\n"% (DstIP, MsgName)
    return text

def SrcPortSet(SrcPort, MsgName):
    text = "\t%s, //%s\n"% (SrcPort, MsgName)
    return text

def DstPortSet(DstPort, MsgName):
    text = "\t%s, //%s\n"% (DstPort, MsgName)
    return text

def MsgIDSet(MsgID, MsgName):
    text = "\t%s, //%s\n"% (MsgID, MsgName)
    return text

def MsgDLCSet(MsgDLC, MsgName):
    text = "\t%s, //%s\n"% (MsgDLC, MsgName)
    return text

def TC_Generate(eNumSet, MsgSet, SrcMAC, DstMAC, SrcIP, DesIP, SrcPort, DstPort, MsgID, MsgDLC):
    text = """/*@!Encoding:949*/
variables
{
  char SRC_ECU_NAME[20];
  long RdbLen;
  long SignitureValue;
  long ICU_Signiture = 1;
  long CLU_Signiture = 2;
  long HUD_Signiture = 4;
  long DVRS_Signiture = 8;
  long ADASPRK_Signiture = 16;
  long RR_CAMERA_Signiture = 32;
  long FR_CAMERA_Signiture = 64;
  long LH_CAMERA_Signiture = 128;
  long RH_CAMERA_Signiture = 256;
  long HU_Signiture = 512;
  float TxTimeValue;
  float RxTimeValue;
  float Timediff;

  long  RDB_Count = 3418;
  byte  ECU_Count = 11;
  byte  ECU_CheckCount = 0;
  long  EthCCHeaderByteOffset = 0;
  long  DLC_ByteOffset = 4;
  long  DATA_ByteOffset = 8;
 
  msTimer Period_10ms;
  msTimer Period_20ms;
  msTimer Period_50ms;
  msTimer Period_100ms;

  long SignitureInfo[11] = 
  {
    0,
    1,
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    256,
    512
  };
  
  char ECU_NAME[11][30] = 
  {
    "ESU" ,
    "ICU"	,
    "CLU"	,
    "HUD"	,
    "DVRS"	,
    "ADAS_PRK"	,
    "RR_CMR"	,
    "SR_FR_CMR"	,
    "SR_SD_CMR_LH"	,
    "SR_SD_CMR_RH"	,
    "H_U"
  };
 
  enum Name{
%s
    IR_MESSAGE_NUM
  };
    
  char Message_NAME[IR_MESSAGE_NUM][100] = 
  {
  // you need to delete with last array ',' to avoid error 
%s
  };

  byte IR_Mac_SrcAddr[IR_MESSAGE_NUM][6]=
  {
  // you need to change to below example style 
  // you need to delete with last array ',' to avoid error
  // {0x02,0x00,0x00,0x00,0x02,0x00}, //example style
%s
  };
  
  byte IR_Mac_DstAddr[IR_MESSAGE_NUM][6]=
  {
    // you need to change to below example style 
    // you need to delete with last array ',' to avoid error
    // {0x01,0x00,0x5e,0x00,0x04,0x80}, //example style
%s
  };
  
  byte ECU_MAC_SrcAddr[10][6] = 
  {
    {	0x02,0x00,0x00,0x00,0x02,0x00	}, //ICU
    {	0x02,0x00,0x00,0x00,0x00,0x80	}, // CLU
    {	0x02,0x00,0x00,0x00,0x00,0x40	}, //HUD
    {	0x02,0x00,0x00,0x00,0x00,0x20	}, //DVRS
    {	0x02,0x00,0x00,0x00,0x00,0x10	}, // ADAS
    {	0x02,0x00,0x00,0x00,0x00,0x08	}, //RR
    {	0x02,0x00,0x00,0x00,0x00,0x04	}, // FR
    {	0x02,0x00,0x00,0x00,0x00,0x02	}, //LH
    {	0x02,0x00,0x00,0x00,0x00,0x01	}, //RH
    {	0x02,0x00,0x00,0x00,0x01,0x00	} //HU
  };

  byte ECU_IP_DstAddr[10][4] = 
  {
    {	10,0,2,0}, //ICU
    {	10,0,0,128}, // CLU
    {	10,0,0,64}, //HUD
    {	10,0,0,32}, //DVRS
    {	10,0,0,16}, // ADAS
    {	10,0,0,8}, //RR
    {	10,0,0,4}, // FR
    {	10,0,0,2}, //LH
    {	10,0,0,1}, //RH
    {	10,0,1,0}
  };
  
  byte IR_IP_SrcAddr[IR_MESSAGE_NUM][4] = 
  {
  // you need to change to below example style 
  // you need to delete with last array ',' to avoid error
  // {0,2,0,10}, //example style
%s
  };
  
  byte IR_IP_DstAddr[IR_MESSAGE_NUM][4] = 
  {
  // you need to change to below example style 
  // you need to delete with last array ',' to avoid error
  // {128,4,0,239}, //example style
%s
  };
  
  long IR_SrcPort[IR_MESSAGE_NUM]=
  {
  // you need to delete with last array ',' to avoid error
%s
  };
  
  long IR_DstPort[IR_MESSAGE_NUM]=
  {
  // you need to delete with last array ',' to avoid error
%s
  };
  
  /*char DST_NAME[IR_MESSAGE_NUM][100] = 
  {
      "ESU, ADAS_PRK",        //4WD11
      "ESU",                  //ADAS_CMD_21_1
      "ESU",                  //ADAS_CMD_31_1
      "ESU, DVRS, ADAS_PRK",  //CLU11
      "ESU",                  //CLU21
      "ESU, ADAS_PRK",        //EMS11
      "ESU, ADAS_PRK",        //EMS12
      "ESU, ADAS_PRK",        //EMS16
      "ESU",                  //EMS20
      "ESU, ADAS_PRK",        //EPB11
      "ESU, ADAS_PRK",        //MDPS11
      "ESU, ADAS_PRK",        //RR_C_RDR_01_1
      "ESU",                  //RR_C_RDR_01_2
      "ESU",                  //RR_C_RDR_02_1
      "ESU, ADAS_PRK",        //RR_C_RDR_02_2
      "ESU, ADAS_PRK",        //TCS11
      "ESU"                   //TCU13
  };*/

  long Message_ID[IR_MESSAGE_NUM] = 
  {
  // you need to delete with last array ',' to avoid error
%s
  };

  long Messgae_DLC[IR_MESSAGE_NUM] = 
  {
  // you need to delete with last array ',' to avoid error
%s
  };
}"""% (eNumSet, MsgSet, SrcMAC, DstMAC, SrcIP, DesIP, SrcPort, DstPort, MsgID, MsgDLC)
    f = open("ECU_InterruptReduction.cin", 'w')

    f.write(text)
    f.close()