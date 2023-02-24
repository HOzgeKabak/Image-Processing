function regionmap = regiongrow3(IN,thresh)

maxdiff = max(max(IN));
maxdiff = maxdiff * thresh;

[a,b] = size(IN);
regionmap = zeros(a,b);

regionvalue = 1;
markj = 0;
markk = 0;
jmet = 0;
kmet = 0;

for k = 1:b
for j = 1:a
  if regionmap(j,k) == 0

    while kmet == 0 && (k+markk) < b && jmet==0 && (j+markj)<a

      temp = IN(j:j+markj, k:k+markk);
      if regionmap(j+markj, k+markk) ~= 0
    	break;
      end
      if (max(max(temp)) - min(min(temp))) < maxdiff
        markk = markk + 1;
	markj = markj + 1;
	else
        jmet = 1;
	kmet = 1;
      end 
    end
    markk = markk - 1;
    if jmet==1 && kmet ==1
      markj = markj - 1;
      temp = IN(j:j+markj, k:k+markk);
      regionmap(j:j+markj, k:k+markk) = mean(mean(temp));
      regionvalue = regionvalue + 1	;
    end
    jmet = 0;
    kmet = 0;
    markj = 0;
    markk = 0;
  end
end
end








