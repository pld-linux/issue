Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(fr):	Fichier de version de PLD Linux
Summary(pl):	Wersja Linuxa PLD.
Summary(tr):	PLD Linux s�r�m dosyas�
Name:		issue
Version:	1.0
Release:	7
Copyright:	free
Group:		Base
Group(pl):	Podstawowe
Buildarch:	noarch
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue-logo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file

%description -l de
PLD Linux Release-Datei

%description -l fr
Fichier de version de PLD Linux.

%description -l pl
Wersja Linuksa PLD.

%description -l tr
PLD Linux s�r�m dosyas�

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
c
 .----------------------< PLD GNU/Linux 1.0 (Ra) >----------------------*
:|:
:|:  Welcome to \n
:|:  \d \t
:|:
 \`---{ \u users }---[ \r ]---(\m)------*

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
 .----------------------< PLD GNU/Linux 1.0 (Ra) >------*
:|:
:|:  Welcome to %h
:|:  %d
:|:
 \`-----------[ %r ]--(%m)------*
 
EOF

echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
