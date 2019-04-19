"""A module for dealing with SNIA DDF RAID sets"""

# Signatures for the on-disk configuration structures
# Defined in section 5.3 of the specification
DDF_Header_Signature =                             bytes([0x11, 0xDE, 0x11, 0xDE])
DDF_Controller_Data_Signature =                    bytes([0x11, 0x11, 0x11, 0xAD])
DDF_Physical_Disk_Record_Signature =               bytes([0x22, 0x22, 0x22, 0x22])
DDF_Physical_Disk_Data_Signature =                 bytes([0x33, 0x33, 0x33, 0x33])
DDF_Virtual_Disk_Record_Signature =                bytes([0xDD, 0xDD, 0xDD, 0xDD])
DDF_Virtual_Disk_Configuration_Record_Signature =  bytes([0xEE, 0xEE, 0xEE, 0xEE])
DDF_Spare_Assignment_Record_Signature =            bytes([0x55, 0x55, 0x55, 0x55])
DDF_Vendor_Unique_Configuration_Record_Signature = bytes([0x88, 0x88, 0x88, 0x88])
DDF_Vendor_Specific_Log_Signature =                bytes([0x0F, 0xEE, 0xDB, 0x01])
DDF_Bad_Block_Management_Log_Signature =           bytes([0x0C, 0xB1, 0xAD, 0xAB])

class DDF_Header:
    """DDF Header as defined in section 5.3 of the SNIA DDF specification"""
    Signature =                             bytes(4)    # 0 - 3
    CRC =                                   bytes(4)    # 4 - 7
    DDF_Header_GUID =                       bytes(24)   # 8 - 31
    DDF_Revision =                          bytes(8)    # 32 - 39
    Sequence_Number =                       bytes(4)    # 40 - 43
    Timestamp =                             bytes(4)    # 44 - 47
    Open_Flag =                             bytes(1)    # 48
    Foreign_Flag =                          bytes(1)    # 49
    Disk_Grouping =                         bytes(1)    # 50
    Reserved0 =                             bytes(13)   # 51 - 63
    Header_Ext =                            bytes(32)   # 64 - 95
    Primary_Header_LBA =                    bytes(8)    # 96 - 103
    Secondary_Header_LBA =                  bytes(8)    # 104 - 111
    Header_Type =                           bytes(1)    # 112
    Reserved1 =                             bytes(3)    # 113 - 115
    Workspace_Length =                      bytes(4)    # 116 - 119
    Workspace_LBA =                         bytes(8)    # 120 - 127
    Max_PD_Entries =                        bytes(2)    # 128 - 129
    Max_VD_Entries =                        bytes(2)    # 130 - 131
    Max_Partitions =                        bytes(2)    # 132 - 133
    Configuration_Record_Length =           bytes(2)    # 134 - 135
    Max_Primary_Element_Entries =           bytes(2)    # 136 - 137
    Reserved2 =                             bytes(54)   # 138 - 191
    Controller_Data_Section =               bytes(4)    # 192 - 195
    Controller_Data_Section_Length =        bytes(4)    # 196 - 199
    Physical_Disks_Records_Section =        bytes(4)    # 200 - 203
    Physical_Disks_Records_Section_Length = bytes(4)    # 204 - 207
    Virtual_Disks_Records_Section =         bytes(4)    # 208 - 211
    Virtual_Disks_Records_Section_Length =  bytes(4)    # 212 - 215
    Configuration_Records_Section =         bytes(4)    # 216 - 219
    Configuration_Records_Section_Length =  bytes(4)    # 220 - 223
    Physical_Disk_Data_Section =            bytes(4)    # 224 - 227
    Physical_Disk_Data_Section_Length =     bytes(4)    # 228 - 231
    BBM_Log_Section =                       bytes(4)    # 232 - 235
    BBM_Log_Section_Length =                bytes(4)    # 236 - 239
    Diagnostic_Space =                      bytes(4)    # 240 - 243
    Diagnostic_Space_Length =               bytes(4)    # 244 - 247
    Vendor_Specific_Logs_Section =          bytes(4)    # 248 - 251
    Vendor_Specific_Logs_Section_Length =   bytes(4)    # 252 - 255
    Reserved3 =                             bytes(256)  # 256 - 511  (This isn't actually defined in the spec.  Just here for completeness's sake)
