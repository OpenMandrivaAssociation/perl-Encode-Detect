%define module  Encode-Detect
%define name    perl-%{module}
%define version 1.00
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release} 
Summary:        An Encode::Encoding subclass that detects the encoding of data
License:        GPL
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Encode/%{module}-%{version}.tar.bz2
Buildrequires:  perl-devel
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(ExtUtils::CBuilder)
Buildrequires:  perl(Data::Dump)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data and then
decodes it using the encoder of the detected charset.

It is similar to Encode::Guess, but does not require the configuration of a set
of expected encodings. Like Encode::Guess, it only supports decoding--it cannot
encode.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE
%{perl_vendorarch}/Encode
%{perl_vendorarch}/auto/Encode
%{_mandir}/*/*


