function isPalindrome(n)
    original_n = n;
    reversed_n = 0;

    while(n > 0)
        digit = mod(n, 10);
        reversed_n = reversed_n * 10 + digit;
        n = floor(n / 10);
    end

    if(original_n == reversed_n)
        disp('The number is a palindrome.');
    else
        disp('The number is not a palindrome.');
    end
end

function sos(n)
    disp('Sum of squares:');
    sum = 0;

    for i = 1:n
        sum = sum + i * i;
    end

    disp(sum);
end

function soswrite(filename, n)
    fileID = fopen(filename, 'w');

    if(fileID == -1)
        disp('Error: Could not open the file.');
        return;
    end

    fprintf(fileID, 'Sum of squares: %d\n', sos(n));
    fclose(fileID);
end

function sospalindrome(n)
    disp('Sum of squares:');
    sum = 0;

    for i = 1:n
        sum = sum + i * i;
    end

    disp(sum);
    isPalindrome(sum);
end

% Main function
n = input('Enter a number: ');
soswrite('sos.txt', n);
sospalindrome(n);