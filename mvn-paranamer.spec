#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-paranamer
Version  : 2.8
Release  : 4
URL      : https://github.com/paul-hammant/paranamer/archive/paranamer-parent-2.8.tar.gz
Source0  : https://github.com/paul-hammant/paranamer/archive/paranamer-parent-2.8.tar.gz
Source1  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer-parent/2.3/paranamer-parent-2.3.pom
Source2  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer-parent/2.7/paranamer-parent-2.7.pom
Source3  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer-parent/2.8/paranamer-parent-2.8.pom
Source4  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.3/paranamer-2.3.jar
Source5  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.3/paranamer-2.3.pom
Source6  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.jar
Source7  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.pom
Source8  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.jar
Source9  : https://repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-paranamer-data = %{version}-%{release}
Requires: mvn-paranamer-license = %{version}-%{release}

%description
# ![ParaNamer](http://paulhammant.com/images/ParaNamer.jpg)
## Method Parameter Name Access for Java*

%package data
Summary: data components for the mvn-paranamer package.
Group: Data

%description data
data components for the mvn-paranamer package.


%package license
Summary: license components for the mvn-paranamer package.
Group: Default

%description license
license components for the mvn-paranamer package.


%prep
%setup -q -n paranamer-paranamer-parent-2.8

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-paranamer
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-paranamer/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.3/paranamer-parent-2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.7/paranamer-parent-2.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.8
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.8/paranamer-parent-2.8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.3/paranamer-2.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.3/paranamer-2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.7
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.7
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.8
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.8
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.3/paranamer-parent-2.3.pom
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.7/paranamer-parent-2.7.pom
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer-parent/2.8/paranamer-parent-2.8.pom
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.3/paranamer-2.3.jar
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.3/paranamer-2.3.pom
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.jar
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.pom
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.jar
/usr/share/java/.m2/repository/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-paranamer/LICENSE.txt
