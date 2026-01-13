FROM dperson/samba
# Creating a public share with sensitive files
RUN mkdir -p /share/public
RUN echo "Employee salaries: \nJohn Doe: $100k\nJane Smith: $120k\nFlag: FLAG{SMB_GUEST_ACC3SS}" > /share/public/notes.txt
EXPOSE 445
CMD ["-s", "public;/share/public;yes;no;yes;all", "-p"]
