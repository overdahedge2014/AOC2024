close all;
clear all;

% basic prep
content = 2:1000;
fileID = fopen('input.txt','r');
formatSpec = '%d';
content = fscanf(fileID,formatSpec,[2,1000])';

% sorting required for part 1, not for part 2
list1 = sort(content(:,1),1);
list2 = sort(content(:,2),1);

% part 1
tot = 0; 
for i = 1:size(list1)
    mini = [list1(i,:); list2(i,:)];
    diff = max(mini) - min(mini);
    tot = tot + diff;
end

disp(tot);

% part 2
tot2 = 0;

for i = 1:1000
    val = list1(i,:);
    for j = 1:1000
        if list2(j) == val
            tot2 = tot2 + val;
        end
    end
end

disp(tot2);