from prettytable import PrettyTable

t = PrettyTable(['Proteins','Length','FirstDomain','LastDomain','FD/Length(%)','LD/Length(%)','AvgNoOfSeq(F&L)','AvgNoOfSeq(All)'])
t.add_row(['Non-Glycosylation','x','Avg=x Out=x In=x','Avg=x Out=x In=x','x','x','-','-'])
t.add_row(['Glycosylation','x','Avg=x Out=x In=x','Avg=x Out=x In=x','x','x','x','x'])
t.add_row(['OnlyFirstDomain','x','Avg=x Out=x In=x','Avg=x Out=x In=x','x','x','x','x'])
t.add_row(['OnlyLastDomain','x','Avg=x Out=x In=x','Avg=x Out=x In=x','x','x','x','x'])
t.add_row(['BothDomainGlyco','x','Avg=x Out=x In=x','Avg=x Out=x In=x','x','x','x','x'])
t.add_row(['NoneDomainGlyco','x','Avg=x Out=x In=x','Avg=x Out=x In=x','x','x','x','x'])
print(t)
