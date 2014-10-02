%% exercise 2.2.1

% Digit number to display
i = 9; 

% Load data
load Data/zipdata.mat

% Extract digits data
X = traindata(:,2:end);
y = traindata(:,1);

% Visualize the i'th digit as an image
I = reshape(X(i,:), [16,16])';
imagesc(I);
colormap(1-gray);
axis image off
title('Digit as a image');
