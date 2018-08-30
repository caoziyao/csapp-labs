//
//  path.hpp
//  scope
//
//  Created by working on 2018/8/31.
//  Copyright © 2018年 working. All rights reserved.
//

#ifndef path_hpp
#define path_hpp

#include <stdio.h>
#include <sstream>
#include <string>

namespace patch {

    template < typename T > std::string
    to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}
#endif /* path_hpp */
