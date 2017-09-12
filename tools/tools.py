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
    if( len(n4) != 18 ):
        print "Erorr: %s\t%s\t len = %d" % ( n1, n4, len(n4))

def FileRead( strFileName, nid ):
    strFName = '%s.xls' % strFileName
    data = xlrd.open_workbook( strFName )
    table = data.sheets()[0]
    nrows = table.nrows
    strFName = "%s.sql" % nid
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

def main():
    print '缤纷年代'
    FileRead( './缤纷年代',   104 )
    print '皇冠国际'
    FileRead( './皇冠国际',   109 )
    print '皇家公馆'
    FileRead( './皇家公馆',   110 )
    print '皇家米克斯'
    FileRead( './皇家米克斯', 126 )
    print '金城明珠'
    FileRead( './金城明珠',   112 )
    print '金世茂'
    FileRead( './金世茂',     115 )
    print '昆山之夜'
    FileRead( './昆山之夜',   118 )
    print '英皇国际'
    FileRead( './英皇国际',   124 )
    print '至尊公馆'
    FileRead( './至尊公馆',   122 )

if __name__=="__main__":
    main()

