Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(fr):	Fichier de version de PLD Linux.
Summary(pl):	Wersja Linuxa PLD.
Summary(tr):	PLD Linux sürüm dosyasý
Name:		issue
Version:	1.1
Release:	2
Copyright:	free
Group:		Base
Group(pl):	Podstawowe
Source:		%{name}
Buildarch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

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
 
if grep -q -e Tornado -e Tsunami /etc/pld-release; then
    echo "1.3 PLD Linux (Tsunami)" > $RPM_BUILD_ROOT/etc/pld-release
    install %{SOURCE0} $RPM_BUILD_ROOT/etc

else 
    echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/pld-release
    echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT/etc/issue
    echo "Kernel \r on an \m" >> $RPM_BUILD_ROOT/etc/issue
fi

ln -sf issue $RPM_BUILD_ROOT/etc/issue.net

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config(noreplace) %attr(644,root,root) /etc/*

%changelog
* Tue Dec 08 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
   [1.1-1d]
-  build for prerelease-1.
