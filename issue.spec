Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(fr):	Fichier de version de PLD Linux.
Summary(pl):	Wersja Linuxa PLD.
Summary(tr):	PLD Linux sürüm dosyasý
Name:		issue
Version:	1.0
Release:	3
Copyright:	free
Group:		Base
Group(pl):	Podstawowe
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file

%description -l de
PLD Linux Release-Datei

%description -l fr
Fichier de version de PLD Linux.

%description
Wersja Linuxa PLD.

%description -l tr
PLD Linux sürüm dosyasý

%install
install -d $RPM_BUILD_ROOT/etc
 
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/pld-release
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/issue
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/issue.net
cat >> $RPM_BUILD_ROOT/etc/issue <<EOF
Kernel \\r on an \\m
EOF
echo "Kernel %r on an %m" >> $RPM_BUILD_ROOT/etc/issue.net

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/etc/pld-release
%config(noreplace) /etc/issue*
