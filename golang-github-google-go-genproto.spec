# https://github.com/google/go-genproto
%global forgeurl        https://github.com/google/go-genproto
%global goipath         google.golang.org/genproto
%global commit          94acd270e44e65579b9ee3cdab25034d33fed608

%gometa

Name:           golang-github-google-go-genproto
Version:        0
Release:        0.9%{?dist}
Summary:        Go generated proto packages
# Detected licences
# - *No copyright* Apache (v2.0) GENERATED FILE at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20181025git94acd27
- Bump to 94acd270e44e65579b9ee3cdab25034d33fed608

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.20180328gitf8c8703
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitf8c8703
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20180328gitf8c8703
- Bump to f8c8703595236ae70fdf8789ecb656ea0bcdcf46
  
* Thu Mar 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git09f6ed2
- Bump to 09f6ed296fc66555a25fe4ce95173148778dfa85
  resolves: #1553067

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.4.20170404git411e09b
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git411e09b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git411e09b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git411e09b
- First package for Fedora
  resolves: #1475778

