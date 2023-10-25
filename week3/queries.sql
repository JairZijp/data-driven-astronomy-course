SELECT p.koi_name, p.radius, s.radius
FROM Star AS s
JOIN Planet AS p USING (kepler_id)
WHERE s.kepler_id IN (
  SELECT kepler_id
  FROM Star
  ORDER BY radius DESC
  LIMIT 5
);

SELECT ROUND(AVG(P.t_eq), 1), MIN(S.t_eff), MAX(S.t_eff)
FROM Star S
JOIN Planet P USING(kepler_id)
WHERE S.t_eff > (
  SELECT AVG(t_eff) FROM Star
);