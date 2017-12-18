%% Hossein Hassani
%% Started @: 23 Dec 2014
%% Last update @: 04 Jan 2015

function textWeighting = calculateTextWeighting(weightingList, word_indices_and_counts)
% CALCULATETEXTWEIGHTING calculates text weighting by multiplication of occurances of each word and their correspondent weightings. The weighting shows the 

vocabList = getVocabList();
n = length(vocabList);  % Total number of words in the dictionary

textWeighting = zeros(2, 1);

for i = 1:n
	if (word_indices_and_counts(i) > 0)
		textWeighting(1) += (weightingList{i,1} * word_indices_and_counts(i));
		textWeighting(2) += (weightingList{i,2} * word_indices_and_counts(i));
end

end
