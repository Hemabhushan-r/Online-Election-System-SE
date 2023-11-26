#retrieve only the ballot nos of the voters who have voted
SELECT V.BALLOTID,V.ELECTIONID,E.ELECTIONNAME,V.CANDIDATEID,C.CANDIDATENAME,V.PARTYID,P.PARTYNAME 
FROM VOTE V INNER JOIN ELECTION E INNER JOIN CANDIDATES C INNER JOIN PARTY P
ON V.ELECTIONID=E.ELECTIONID AND V.CANDIDATEID=C.CANDIDATEID AND V.PARTYID=P.PARTYID
WHERE V.VOTESTATUS='YES'
order by electionid;

#get total no. of votes received by each candidate in each election

SELECT v.electionid,
       e.electionname,
       v.candidateid,
       c.candidatename,
       p.PartyName,
       COUNT(v.candidateid) AS Total_Votes
FROM vote v
INNER JOIN Candidates c
   ON v.CandidateID = c.candidateid
INNER JOIN Election e
   ON v.ElectionID = e.electionid
INNER JOIN Party p
   ON v.partyid = p.partyid
WHERE v.candidateid IS NOT NULL
  AND v.VoteStatus = 'yes'
GROUP BY v.electionid,
         v.candidateid,
         p.PartyName
ORDER BY v.electionID ASC,
         COUNT(v.candidateid) DESC;





