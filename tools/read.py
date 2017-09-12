#coding=utf-8
import time
import xlrd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def StrToTime( strTime ):
    arrTime = time.strptime( strTime, "%Y.%m.%d" )
    return int( time.mktime( arrTime ) )

def FuncSex( sex ):
    if( sex == "男" ):
        return 1
    return 0

def FuncSTime( strtime ):
    strt    = strtime.replace('—','-')
    strt    = strt.replace('--','-')
    strt    = strt.replace('--','-')
    strt    = strt.replace('---','-')
    arrstr  = strt.split('-')
    nSTime  = StrToTime( arrstr[0].encode('utf-8') )
    nETime  = StrToTime( arrstr[1].encode('utf-8') )
    return [ nSTime, nETime ]

def FuncPhone( strPhone ):
    return str( int( strPhone ) )

def FuncAddress( strAddress ):
    if( len( strAddress) < 2 ):
        return "前进中路216号(娱乐协会)"
    return strAddress

def CreateSQL( nid, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 ):
 
    Insert = "INSERT INTO UserInfo( nPlaceId,strName,strAlias,nSex,nNumeId,strArea,strPost, \
                nConStart,nConStop,strPhone,strAddre,strNowAd,nStart ) VALUES ( "
    nsex    = FuncSex( n3 )         #性别处理
    at      = FuncSTime( n7 )       #时间处理
    ph      = FuncPhone( n8 )       #处理手机号码
    a1      = FuncAddress( n9 )     #处理地址
    a2      = FuncAddress( n10 )    #处理地址
    Values = "%d,'%s','%s',%d,'%s','%s','%s',%d,%d,'%s','%s','%s', 0 );\n" % (nid,n1,n2,nsex,n4,n5,n6,at[0],at[1],ph,a1,a2 )
    return "%s%s" % ( Insert, Values )


def FileRead( strFileName, nid ):
    strFName = '%s.xls' % strFileName
    data = xlrd.open_workbook( strFName )
    table = data.sheets()[0]
    nrows = table.nrows
    strFName = "%s.sql" % nid
    fo = open( strFName, "a+" )
    for i in range( 3, nrows ):
        strSQL = CreateSQL( nid,
                            table.row( i )[ 1 ].value,
                            table.row( i )[ 2 ].value,
                            table.row( i )[ 3 ].value,
                            table.row( i )[ 4 ].value,
                            table.row( i )[ 5 ].value,
                            table.row( i )[ 6 ].value,
                            table.row( i )[ 7 ].value,
                            table.row( i )[ 8 ].value,
                            table.row( i )[ 9 ].value,
                            table.row( i )[10 ].value
                            )
        fo.write( strSQL )
    fo.close()

def main():
    FileRead( './缤纷年代',   104 )
    FileRead( './皇冠国际',   109 )
    FileRead( './皇家公馆',   110 )
    FileRead( './皇家米克斯', 126 )
    FileRead( './金城明珠',   112 )
    FileRead( './金世茂',     115 )
    FileRead( './昆山之夜',   118 )
    FileRead( './英皇国际',   124 )
    FileRead( './至尊公馆',   122 )

if __name__=="__main__":
    main()

