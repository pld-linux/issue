Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(fr):	Fichier de version de PLD Linux
Summary(pl):	Wersja Linuksa PLD
Summary(tr):	PLD Linux s�r�m dosyas�
Name:		issue
Version:	2.0
Release:	0.1
License:	GPL
Group:		Base
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue-alpha
Obsoletes:	issue-fancy
Obsoletes:	issue-logo
Obsoletes:	issue-pure

%description
PLD Linux release file.

%description -l de
PLD Linux Release-Datei.

%description -l fr
Fichier de version de PLD Linux.

%description -l pl
Wersja Linuksa PLD.

%description -l tr
PLD Linux s�r�m dosyas�.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
c
 .------------------------< PLD Linux 1.0 (Ra) >------------------------*
:|:
:|:  Welcome to \n
:|:  \d \t
:|:
 \`---{ \U }---[ \r ]---( \m )------*


EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
 .------------------------< PLD Linux 2.0 (Ac) >--------*
:|:
:|:  Welcome to %h
:|:  %d
:|:
 \`-----------[ %r ]--( %m )------*

EOF

echo "2.0 PLD Linux (Ac)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
